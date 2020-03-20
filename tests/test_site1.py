
import os
from lib.http import TestHTTP 


class Test(TestHTTP):

    def setUp(self):

        super().setUp('''
        error_log  logs/error.log debug;
        events {}
        http {
            lua_package_path '/usr/local/nginx/lua/?.lua;;';
            lua_package_cpath '/usr/local/nginx/lua/?.so;;';
            server {
                listen  127.0.0.1:7080;

                location / {
                    content_by_lua_block {
                        local m = require("site1");
                        m.auth(ngx.var.remote_addr);
                    }
                }

                location /auth {
                    content_by_lua_block {
                        local m = require("site1");
                        m.auth('1.1.1.1');
                    }
                }
            }
        }
        ''')

    def test_auth(self):
        self.assertEqual(self.get()['status'], 200, 'passed')
        self.assertEqual(self.get(url = '/auth')['status'], 403, 'forbidden')


if __name__ == '__main__':
    Test.main()
