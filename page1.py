from flask import Flask, request, render_template
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg

app = Flask(__name__, static_folder='images')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

def renderTemperatureGraph(x, temperatures):
    figure = Figure()
    canvas = FigureCanvasAgg(figure)
    graph = figure.add_subplot(1, 1, 1)
    graph.plot(x, temperatures)
    figure.savefig('./images/temp_graph.png')


def renderRevenueGraph(x, revenues):
    figure = Figure()
    canvas = FigureCanvasAgg(figure)
    graph = figure.add_subplot(1, 1, 1)
    graph.plot(x, revenues)
    figure.savefig('./images/revenue_graph.png')

@app.route('/result')
def result():
    person = {'name': 'steve', 'address': 'USA', 'phone': '+123423243'}
    products = [
        {'title': 'product1', 'price': 100, 'description': 'a nice product 1'},
        {'title': 'product2', 'price': 200, 'description': 'a nice product 2'},
        {'title': 'product3', 'price': 300, 'description': 'a nice product 3'},
        {'title': 'product4', 'price': 400, 'description': 'a nice product 4'},
        {'title': 'product5', 'price': 500, 'description': 'a nice product 5'},
        {'title': 'product6', 'price': 600, 'description': 'a nice product 6'},
    ]

    # for product in products:
    #     print(product['title'])

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    temperatures = [29, 28, 30, 21, 22, 25, 26, 28, 30, 32, 25, 28]
    revenues = [100, 200, 250, 150, 300, 200, 240, 500, 350, 450, 300, 200]


    # temp graph
    renderTemperatureGraph(x, temperatures)

    # revenue graph
    renderRevenueGraph(x, revenues)

    return render_template('result.html', personInfo=person, products=products,
                           temperatures=temperatures,
                           revenues=revenues,
                           temperatureFile='/images/temp_graph.png',
                           revenueFile='/images/revenue_graph.png')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    # 1-1024: reserved by IANA
    app.run(debug=True, port=6500, host='0.0.0.0')
