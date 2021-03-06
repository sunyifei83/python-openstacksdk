# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack.orchestration.v1 import stack
from openstack import proxy
from openstack import resource


class Proxy(proxy.BaseProxy):

    def create_stack(self, **data):
        return stack.Stack(data).create(self.session)

    def find_stack(self, name_or_id):
        return stack.Stack.find(self.session, name_or_id)

    def list_stacks(self):
        return stack.Stack.list(self.session)

    def get_stack(self, **data):
        return stack.Stack(data).get(self.session)

    def delete_stack(self, value, ignore_missing=True):
        """Delete a stack

        :param value: The value can be either the ID of a stack or a
                      :class:`~openstack.orchestration.v1.stack.Stack`
                      instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the stack does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent server.

        :returns: ``None``
        """
        self._delete(stack.Stack, value, ignore_missing)

    def wait_for_stack(self, value, status='CREATE_COMPLETE',
                       failures=['CREATE_FAILED'], interval=2, wait=120):
        return resource.wait_for_status(self.session, value, status,
                                        failures, interval, wait)
