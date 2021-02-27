---

date: 2013-09-13
slug: |
  using-python-to-control-katello
tags:
 - katello
 - english
 - python
title: Using Python to Control Katello
---

![Emacs editor with python code](http://bit.ly/14Q0fhi)

I usually like to use python to script my day to day tests against
[Katello](http://www.katello.org/) (you may have seen some of my
[previous](http://ogmaciel.tumblr.com/post/52170839167/populating-a-katello-instance-using-the-cli)
[posts](http://ogmaciel.tumblr.com/post/29571582261/script-to-populate-a-katello-instance-with-valid-data)
about using the Katello CLI for the same purpose) and I figured I'd
start showing some basic examples for anyone else out there who may be
interested.

Assuming you have already installed and configured your Katello instance
(learn how to do this
[here](https://fedorahosted.org/katello/wiki/Install)) with the default
configurations, we now have a few options to proceed:

1.  write and run your scripts in the same environment as your server
2.  install the [katello-cli](https://pypi.python.org/pypi/katello-cli/)
    package (*pip install katello-cli*)
3.  Use git to clone the katello-cli
    [repository](https://github.com/Katello/katello-cli) (*git
    clone https://github.com/Katello/katello-cli.git*) and make sure to
    include it into your **PYTHONPATH**.

**Option 1** is by far the easiest approach since you should have all
the dependencies (namely **kerberos** and **M2Crypto**) already
installed, but I like **Option 3** as it allows me to always have the
latest code to play with.

Now we're ready to write some code! The first thing we'll do is import
some of the Katello modules:

>  from katello.client import server  from katello.client.server import
> BasicAuthentication  from katello.client.api.organization import
> OrganizationAPI  from katello.client.api.system_group import
> SystemGroupAPI

Next, we establish a connection to the Katello server
(**qetello01.example.com** in my case), using the default credentials of
**admin**/**admin**:

```shell
> katello_server = server.KatelloServer(host='qetello01.example.com',
> path_prefix='/katello/', port=443)
> katello_server.set_auth_method(BasicAuthentication(username='admin',
> password='admin')) server.set_active_server(katello_server)
```
 

Let's now instantiate the Organization API object and use it to fetch
the "**ACME_Corporation**" that gets automatically created for a
default installation:

 
```shell
> organization_api = OrganizationAPI()
>
> org = organization_api.organization(\'ACME_Corporation\') print org
> {u'apply_info_task_id': None, u'created_at': u'2013-09-12T20:15:06Z',
> u'default_info': {u'distributor': \[\], u'system': \[\]},
> u'deletion_task_id': None, u'description': u'ACME_Corporation
> Organization', u'id': 1, u'label': u'ACME_Corporation', u'name':
> u'ACME_Corporation', u'owner_auto_attach_all_systems_task_id': None,
> u'service_level': None, u'service_levels': \[\], u'updated_at':
> u'2013-09-12T20:15:06Z'}
```


Lastly, let's create a brand new organization:

 
```shell
> new_org = organization_api.create(name=\'New Org\', label=\'new-org\',
> description=\'Created via API\') print new_org {u'apply_info_task_id':
> None, u'created_at': u'2013-09-12T21:48:55Z', u'default_info':
> {u'distributor': \[\], u'system': \[\]}, u'deletion_task_id': None,
> u'description': u'Created via API', u'id': 283, u'label': u'new-org',
> u'name': u'New Org', u'owner_auto_attach_all_systems_task_id': None,
> u'service_level': None, u'service_levels': \[\], u'updated_at':
> u'2013-09-12T21:48:55Z'}
``` 

As you can see, it is pretty straight forward to use python to create
some useful scripts to drive a Katello server, whether you want to
populate it with a pre-defined set of data (e.g. default users, roles,
permissions, organizations, content, etc) or to test core functionality
as I do with [Mangonel](https://github.com/omaciel/mangonel), my pet
project.

Here's a [Gist](https://gist.github.com/anonymous/71c0527841d30b80424b)
of the code mentioned in this post, and let me know if this was useful
to you.
