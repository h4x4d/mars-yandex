import flask
from flask import jsonify, request

from data import db_session
from data.__all_models import *

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs', methods=['GET', 'POST'])
def get_jobs():
    db_sess = db_session.create_session()
    if request.method == 'GET':
        news = db_sess.query(Jobs).all()
        return jsonify(
            {
                'jobs':
                    [item.to_dict() for item in news]
            }
        )
    else:
        if not all(key in request.json for key in
                 ['id', 'team_leader', 'job', 'work_size', 'collaborators']):
            return jsonify({})

        check = db_sess.query(Jobs).filter(Jobs.id == request.json['id']).first()

        if check:
            return jsonify({'error': 'Id already exists'})

        r = request.json
        if type(r['id']) != int or type(r['team_leader']) != int or type(r['work_size']) != int:
            return jsonify({'error': 'Datatype Mismatch'})
        job = Jobs()
        job.id = r['id']
        job.team_leader = r['team_leader']
        job.job = r['job']
        job.work_size = r['work_size']
        job.collaborators = r['collaborators']
        db_sess.add(job)
        db_sess.commit()

        return jsonify({'success': True})


@blueprint.route('/api/jobs/delete/<job_id>', methods=['DELETE'])
def del_jobs(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.id == job_id).first()
    if not job:
        return jsonify({})
    db_sess.delete(job)
    db_sess.commit()
    return jsonify({'Success': True})


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
