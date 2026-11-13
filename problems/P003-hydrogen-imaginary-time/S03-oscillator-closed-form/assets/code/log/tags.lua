-- tags.lua -- provenance tags written as inline code (`[D]`, `[S]`, `[A2]`, ...) become the
-- margin-note macros of the house template; inside headings they become plain text "[N]"
-- (a margin note inside \section is fragile). Nothing else is touched.
local function tagof(s) return s:match("^%[([DSVRAN%?]%d*)%]$") end

local in_header = {
  Header = function(h)
    return h:walk({ Code = function(c)
      local t = tagof(c.text)
      if t then return pandoc.Str("[" .. t .. "]") end
    end })
  end
}

local macros = { D = "\\Dtag{}", R = "\\Rtag{}", N = "\\Ntag{}", ["?"] = "\\Qtag{}",
                 S = "\\Stag{}", V = "\\Vtag{}", A = "\\Atag{}" }
local elsewhere = {
  Code = function(c)
    local t = tagof(c.text)
    if not t then return nil end
    if macros[t] then return pandoc.RawInline("latex", macros[t]) end
    return pandoc.RawInline("latex", "\\tagmark{[" .. t .. "]}")   -- A1, A2, A3
  end
}
return { in_header, elsewhere }
