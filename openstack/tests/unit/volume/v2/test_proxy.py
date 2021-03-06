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

from openstack.tests.unit import test_proxy_base
from openstack.volume.v2 import _proxy
from openstack.volume.v2 import snapshot
from openstack.volume.v2 import type
from openstack.volume.v2 import volume


class TestVolumeProxy(test_proxy_base.TestProxyBase):
    def setUp(self):
        super(TestVolumeProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

    def test_snapshot_delete(self):
        self.verify_delete2(snapshot.Snapshot, self.proxy.delete_snapshot,
                            False)

    def test_snapshot_delete_ignore(self):
        self.verify_delete2(snapshot.Snapshot, self.proxy.delete_snapshot,
                            True)

    def test_type_delete(self):
        self.verify_delete2(type.Type, self.proxy.delete_type, False)

    def test_type_delete_ignore(self):
        self.verify_delete2(type.Type, self.proxy.delete_type, True)

    def test_volume_delete(self):
        self.verify_delete2(volume.Volume, self.proxy.delete_volume, False)

    def test_volume_delete_ignore(self):
        self.verify_delete2(volume.Volume, self.proxy.delete_volume, True)

    def test_volume_get(self):
        self.verify_get('openstack.volume.v2.volume.Volume.get',
                        self.proxy.get_volume)
