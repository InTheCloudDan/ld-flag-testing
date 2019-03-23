#!/usr/bin/env python3
from flask import Flask, request, render_template
import logging
from flask.logging import default_handler
import sys
import os
import atexit
import ldclient

app = Flask(__name__)


def on_exit():
    ldclient.get().close()


@app.route('/')
def basic_route():
    user = {
        "key": "bob@example.com",
        "custom": {
            "groups": "beta_testers"
        }
    }
    show_feature = ldclient.get().variation("test-flag", user, False)
    client_response = "Feature is enabled!" if show_feature else "Not enabled!"
    return client_response


@app.route('/canary')
def canary_route():
    customer_type = request.args.get('customer_type')
    if customer_type == 'internal_qa':
        user = {
            "key": "internal_testing",
            "custom": {
                "groups": "beta_testers"
            }
        }
    else:
        user = {
            "key": "random_visitor"
        }

    show_feature = ldclient.get().variation("internal-customers", user, False)
    client_feature = True if show_feature == 'qa_enabled' else False

    return render_template('user.html', show_feature=client_feature)


if __name__ == "__main__":
    # Use example logging https://github.com/launchdarkly/hello-python
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)
    # Log Flask to same handler
    root.addHandler(default_handler)

    # Setup LD Client
    ld_client_key = os.environ.get('LD_KEY')
    ldclient.set_sdk_key(ld_client_key)
    atexit.register(on_exit)

    # Starting Flask server
    app.run()
