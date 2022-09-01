# Running test code
## Install dependencies
```
pip install -r requirements.txt
```

## Spin up database
```
docker compose up
```

## Run migrations
```
python manage.py migrate
```

## Generate some test data
```
python manage.py gen_data
```

## Recreating the bug
To recreate the bug, first start the development server:
```
python manage.py runserver
```

Next, navigate to http://localhost:8000/company, which will trigger the bug.
The bug has the following stack trace:
```
Internal Server Error: /company/
Traceback (most recent call last):
  File "~/django-safedelete-bug/venv/lib/python3.10/site-packages/django/db/models/sql/query.py", line 1433, in build_filter
    join_info = self.setup_joins(
  File "~/django-safedelete-bug/venv/lib/python3.10/site-packages/django/db/models/sql/query.py", line 1808, in setup_joins
    path, final_field, targets, rest = self.names_to_path(
  File "~/django-safedelete-bug/venv/lib/python3.10/site-packages/django/db/models/sql/query.py", line 1733, in names_to_path
    raise MultiJoin(pos + 1, names_with_path)
django.db.models.sql.datastructures.MultiJoin: (1, [('billing_location_for_company', [PathInfo(from_opts=<Options for Location>, to_opts=<Options for Company>, target_fields=(<django.db.models.fields.BigAutoField: id>,), join_field=<ManyToOneRel: company.company>, m2m=True, direct=False, filtered_relation=None)])])

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "~/django-safedelete-bug/venv/lib/python3.10/site-packages/django/core/handlers/exception.py", line 55, in inner
    response = get_response(request)
  File "~/django-safedelete-bug/venv/lib/python3.10/site-packages/django/core/handlers/base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "~/django-safedelete-bug/safedeletebug/company/views.py", line 6, in index
    locations = Location.objects.filter(
  File "~/django-safedelete-bug/venv/lib/python3.10/site-packages/django/db/models/query.py", line 1428, in exclude
    return self._filter_or_exclude(True, args, kwargs)
  File "~/django-safedelete-bug/venv/lib/python3.10/site-packages/django/db/models/query.py", line 1438, in _filter_or_exclude
    clone._filter_or_exclude_inplace(negate, args, kwargs)
  File "~/django-safedelete-bug/venv/lib/python3.10/site-packages/django/db/models/query.py", line 1443, in _filter_or_exclude_inplace
    self._query.add_q(~Q(*args, **kwargs))
  File "~/django-safedelete-bug/venv/lib/python3.10/site-packages/django/db/models/sql/query.py", line 1532, in add_q
    clause, _ = self._add_q(q_object, self.used_aliases)
  File "~/django-safedelete-bug/venv/lib/python3.10/site-packages/django/db/models/sql/query.py", line 1562, in _add_q
    child_clause, needed_inner = self.build_filter(
  File "~/django-safedelete-bug/venv/lib/python3.10/site-packages/django/db/models/sql/query.py", line 1451, in build_filter
    return self.split_exclude(filter_expr, can_reuse, e.names_with_path)
  File "~/django-safedelete-bug/venv/lib/python3.10/site-packages/django/db/models/sql/query.py", line 2029, in split_exclude
    condition, needed_inner = self.build_filter(Exists(query))
  File "~/django-safedelete-bug/venv/lib/python3.10/site-packages/django/db/models/expressions.py", line 1476, in __init__
    super().__init__(queryset, **kwargs)
  File "~/django-safedelete-bug/venv/lib/python3.10/site-packages/django/db/models/expressions.py", line 1423, in __init__
    self.query = getattr(queryset, "query", queryset).clone()
  File "~/django-safedelete-bug/venv/lib/python3.10/site-packages/safedelete/query.py", line 66, in clone
    clone._safedelete_visibility = self._safedelete_visibility
AttributeError: 'SafeDeleteQuery' object has no attribute '_safedelete_visibility'
[01/Sep/2022 15:10:51] "GET /company/ HTTP/1.1" 500 133651
```