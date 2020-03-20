
-- copyright (C) nginxlab <nginxlab@gmail.com>


local _M = {};


function _M.auth(ip)
    if (ip ~= '127.0.0.1') then
        ngx.exit(ngx.HTTP_FORBIDDEN);
    end
end


return _M;
