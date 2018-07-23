#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from oslo_policy import policy


rules = [
    policy.RuleDefault('shared_address_scopes',
                       'field:address_scopes:shared=True',
                       description='Rule of shared address scope'),
    policy.RuleDefault('create_address_scope',
                       '',
                       description='Access rule for creating address scope'),
    policy.RuleDefault('create_address_scope:shared',
                       'rule:admin_only',
                       description=('Access rule for creating '
                                    'shared address scope')),
    policy.RuleDefault('get_address_scope',
                       'rule:admin_or_owner or rule:shared_address_scopes',
                       description='Access rule for getting address scope'),
    policy.RuleDefault('update_address_scope',
                       'rule:admin_or_owner',
                       description='Access rule for updating address scope'),
    policy.RuleDefault('update_address_scope:shared',
                       'rule:admin_only',
                       description=('Access rule for updating '
                                    'shared attribute of address scope')),
    policy.RuleDefault('delete_address_scope',
                       'rule:admin_or_owner',
                       description='Access rule for deleting address scope')
]


def list_rules():
    return rules
