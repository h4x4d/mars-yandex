import flask
from flask import jsonify

from data import db_session
from data.__all_models import *

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict() for item in news]
        }
    )


@blueprint.route('/api/jobs/<job_id>', methods=['GET'])
def get_job(job_id):
    if not job_id.isdigit():
        return {}
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.id == job_id).first()
    if job:
        return jsonify(
            {
                'jobs': job.to_dict()
            }
        )
    return jsonify({})


def main():
    app = flask.Flask(__name__)
    db_session.global_init("db/data.db")
    app.register_blueprint(blueprint)
    app.run()


if __name__ == '__main__':
    main()
