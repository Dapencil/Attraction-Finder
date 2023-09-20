from flask import Flask, request, render_template, redirect
from dotenv import load_dotenv
import os
import json
from search_util import SearchUtil
from agent import MyAgent

load_dotenv()
open_ai_key = os.getenv("OPEN_AI_KEY")
search_key = os.getenv("SERP_API_KEY")
model_name = "gpt-3.5-turbo"

search_util = SearchUtil(api_key=search_key)
agent = MyAgent(api_key=open_ai_key,model_name=model_name)

cur_db = []

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/confirm",methods=['POST'])
def confirm_page():
    user_text = request.form.get("user-text")
    specification = agent.extract_info(user_text)
    if specification['place'] == None:
        return render_template("error.html")
    return render_template("confirmation.html",
                           place=specification['place'],
                           description=specification['description'],
                           season=specification['season'],
                           user_msg=user_text)

@app.route("/retry",methods=['POST'])
def retry_page():
    return render_template("retry.html",
                           place=request.form.get("place"),
                           description=request.form.get("description"),
                           season=request.form.get("season"),
                           user_msg=request.form.get("user_msg"))

@app.route("/sendRetry",methods=['POST'])
def retry_extract():
    reference_text = request.form.get("user_msg")
    feedback = request.form.get("feedback_msg")

    specification = {
        'place': request.form.get("place"),
        'description': request.form.get("description"),
        'season': request.form.get("season")
    }
    specification = agent.retry_extract(specification=specification
                                        ,reference_text=reference_text,
                                        feedback_text=feedback)

    if specification['place'] == None:
        return render_template("error.html")
    return render_template("confirmation.html",
                           place=specification['place'],
                           description=specification['description'],
                           season=specification['season'],
                           user_msg=reference_text)

@app.route("/getAtts",methods=["POST"])
def get_list_att():
    global cur_db
    specification_json = json.dumps(request.form)
    att_list = agent.find_atts_chain(spec_msg=specification_json)
    for index in range(len(att_list)):
        print('Search Image:',index)
        att = att_list[index]
        att['ori_index'] = index
        image = search_util.get_image_of(att['name'],750,500,16/9)
        att['src'] = image['src']
    cur_db = list(att_list)
    return redirect("/show/0")

@app.route("/show/<int:index>",methods=['GET'])
def show_page(index):
    others_att = list(cur_db)
    others_att.pop(index)
    return render_template("showAtt.html",
                           cur_att=cur_db[index],
                           others_att=others_att)

if __name__ == "__main__":
    app.run(debug=True)
