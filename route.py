from flask import Flask, render_template, request, redirect
from searchquery import search

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/search')

@app.route('/search', methods=['GET', 'POST'])
def ui_search():
    if request.method == 'POST':
        query = request.form['searchTerm']
        fields = list(request.form.keys())
        operator = request.form['operator']
        fields.remove('searchTerm')
        fields.remove('operator')

        res = search(query, fields, operator)
        
        hits = res['hits']['hits']
        time = res['took']
        num_results =  res['hits']['total']['value']
        
        print(query,fields,operator)
        return render_template('index.html', query=query, hits=hits, num_results=num_results, time=time)

    else:
        return render_template('index.html', init='True')

@app.errorhandler(404)
def page_not_found(e):
    return redirect('/search')

if __name__ == '__main__':
    app.run(debug=True)
