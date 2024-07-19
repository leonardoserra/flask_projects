from flask import Flask, render_template
import routes

def create_app():
  app = Flask(__name__)

  # @app.route('/home')
  # @app.route('/')
  # def home():
  #   return render_template('base.html', title='TITOLONE', subtitle="Sono il Subtitle")
  return app

