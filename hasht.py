datathing = [{
    "status": "good",
    "body": "Everything operating normally.",
    "created_on": "2016-01-21T20:28:31Z"
}, {
    "status": "minor",
    "body": "We're investigating issues serving GitHub pages.",
    "created_on": "2016-01-21T20:25:03Z"
}, {
    "status": "good",
    "body": "Everything operating normally.",
    "created_on": "2016-01-20T22:56:57Z"
}, {
    "status": "minor",
    "body": "We're investigating issues affecting a small number of repositories.",
    "created_on": "2016-01-20T22:47:07Z"
}]
for d in datathing:
  print(d['created_on'], '--',
        d['status'] + ':')
  print(d['body'])
  print("")
for d in datathing:
    if d['status']=='good':
        print d['status']