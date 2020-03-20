
-- copyright (C) nginxlab <nginxlab@gmail.com>


local _M = {};


function _M.new()
    local self = {
        sum = 0
    };

    return setmetatable(self, {__index = _M});
end


function _M.add(self, v)
    self.sum = self.sum + v;
    return self.sum;    
end


return _M;
