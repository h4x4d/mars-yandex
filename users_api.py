import flask
from flask import jsonify, request

from data import db_session
from data.__all_models import *

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    if not user_id.isdigit():
        return {}
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == user_id).first()
    if user:
        return jsonify(
            {
                'user': user.to_dict()
            }
        )
    return jsonify({})


@blueprint.route('/api/users', methods=['GET', 'POST'])
def get_user():
    db_sess = db_session.create_session()
    if request.method == 'GET':
        users = db_sess.query(Jobs).all()
        return jsonify(
            {
                'users': [item.to_dict() for item in users]
            }
        )
    else:
        if not all(key in request.json for key in
                 ['id', 'name', 'surname', 'age', 'position', 'speciality',
                  'email', 'hashed_password', 'address']):
            return jsonify({})

        check = db_sess.query(User).filter(User.id ==
                                           request.json['id']).first()

        if check:
            return jsonify({'error': 'Id already exists'})

        r = request.json
        if type(r['id']) != int or type(r['age']) != int:
            return jsonify({'error': 'Datatype Mismatch'})
        user = User()
        for key in r.keys():
            exec(f'user.{key} = r["{key}"]')
        db_sess.add(user)
        db_sess.commit()

        return jsonify({'success': True})


@blueprint.route('/api/users/edit/<user_id>', methods=['GET', 'POST'])
def edit_jobs(user_id):
    db_sess = db_session.create_session()

    job = db_sess.query(User).filter(User.id == int(user_id)).first()
    r = dict(request.json)
    for key in r.keys():
        exec(f'job.{key} = r["{key}"]')
    db_sess.commit()

    return jsonify({'success': True})


@blueprint.route('/api/users/delete/<user_id>', methods=['DELETE'])
def del_user(user_id):
    if not user_id.isdigit():
        return jsonify({'error': 'Datatype Mismatch'})
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == user_id).first()
    if not user:
        return jsonify({'error': 'Not exists'})
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'Success': True})


def main():
    app = flask.Flask(__name__)
    db_session.global_init("db/data.db")
    app.register_blueprint(blueprint)
    app.run()


if __name__ == '__main__':
    main()
