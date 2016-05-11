# lago-dsl
This script executes lagopus DSL directly.
You can add/modify/delete/dump flows without OpenFlow controller.

## How to use

```
$ ./lago-dsl.py [lagopus DSL]
```

- sample
```
$ ./lago-dsl.py flow bridge01
[{u'tables': [{u'table': 0, u'flows': [{u'hard_timeout': 0, u'actions': [{u'apply_actions': [{u'output': 2}]}], u'priority': 100, u'idle_timeout': 0, u'cookie': 0, u'in_port': 1}, {u'hard_timeout': 0, u'actions': [{u'apply_actions': [{u'output': 1}]}], u'priority': 100, u'idle_timeout': 0, u'cookie': 0, u'in_port': 2}]}], u'name': u'bridge01'}]
```

### lagopus DSL syntax
  - See https://github.com/lagopus/lagopus/blob/master/docs/how-to-use-ds-flow-cmd.md

