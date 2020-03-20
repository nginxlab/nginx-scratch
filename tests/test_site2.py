
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
                        local math = require("site2").new();
                        local sum = math:add(10);
                        ngx.print(sum);
                    }
                }
            }
        }
        ''')

    def test_auth(self):
        self.assertEqual(self.get()['status'], 200, 'status')
        self.assertEqual(self.get()['body'], '10', 'body')


if __name__ == '__main__':
    Test.main()
