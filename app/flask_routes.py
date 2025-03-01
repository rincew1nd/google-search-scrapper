from flask import render_template, request, jsonify

def register_routes(app, google_searcher):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/search', methods=['POST'])
    def search():
        query = request.form.get('query', '')
        results = google_searcher.search(query)
        return jsonify(results)