
Tests
=====

Tests are comprised of the following options in a yaml or json document.

Options | Description
-------------|------------
name \* | name for the test
uri \* | /url/path/to/resource.json
protocol | tcp, http, https or noop
port | 0 - 65535
method | GET, POST, PUT, DELETE, OPTION
[inputs.md](inputs) | Inputs accept all verbs that requests does, in the same format for convenience. See below for details.
[outcomes.md](outcomes) | Outcomes is a list of tests to run against the response. See below for details.
