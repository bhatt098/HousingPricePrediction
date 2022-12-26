from flask import Flask

app=Flask(__name__)

@app.route('/',methods=['Get','Post'])
def run():
    return 'testing '



if __name__ == "__main__":
    app.run()