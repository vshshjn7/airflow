#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""sla miss execution_time on update current time fix

Revision ID: a982338e6d7f
Revises: 0e2a74e0fc9f
Create Date: 2020-09-01 13:48:03.093594

"""

# revision identifiers, used by Alembic.
revision = 'a982338e6d7f'
down_revision = '0e2a74e0fc9f'
branch_labels = None
depends_on = None

from alembic import op
from sqlalchemy.dialects import mysql
from sqlalchemy import text


def upgrade():
    conn = op.get_bind()
    if conn.dialect.name == "mysql":
        op.alter_column(table_name='sla_miss', column_name='execution_date',
            type_=mysql.TIMESTAMP(fsp=6), nullable=False,
            server_default=text('CURRENT_TIMESTAMP(6)'))


def downgrade():
    pass
