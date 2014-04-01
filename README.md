Bottle on OpenShift
===================

A quickstart for Bottle + Python 2.6 running on OpenShift. Based on the OpenShift-authored version here: https://github.com/openshift-quickstart/bottle-openshift-quickstart


Running on OpenShift
----------------------------

Create an account at https://www.openshift.com/

Create a python application

    rhc app create bottle python-2.6

Add this upstream bottle repo

    cd bottle
    git remote add upstream -m master git://github.com/kallimachos/openshift_bottle.git
    git pull -s recursive -X theirs upstream master

Then push the repo upstream

    git push

That's it, you can now checkout your application at:

    http://bottle-$yournamespace.rhcloud.com
