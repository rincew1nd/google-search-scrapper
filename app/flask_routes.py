from flask import render_template, request, jsonify, send_file
from app.file_manager import save_file


def register_routes(app, google_searcher):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/search', methods=['POST'])
    def search():
        query = request.form.get('query', '')
        results = google_searcher.search(query)
        filename = f"{query.replace(' ', '_')}.json"
        save_file(results, filename)
        return jsonify({ 'results': results, 'filename': filename })    

    @app.route('/history/<path:filename>', methods=['GET'])
    def download_file(filename):
        try:
            return send_file(f'history/{filename}', as_attachment=True)
        except FileNotFoundError:
            return jsonify({'error': 'File not found.'}), 404