from app import app


@app.route("/new", methods=['POST'])
def add_record():
    # TODO: an endpoint to add new movie/show review
    pass


@app.route("/delete/<int:id>")
def delete_record(id):
    # TODO: an endpoint to delete a particular movie/show
    pass


@app.route("/update/<int:id>")
def update_record(id):
    # TODO: an endpoint to update the existing movie/show record
    pass


@app.route("/get/<int:id>", methods=['GET'])
def get_record(id):
    # TODO: an endpoint to fetch available records
    pass
