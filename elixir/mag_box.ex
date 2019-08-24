defmodule Magnet do

    def doubles(maxk, maxn) do
     vkn = fn k, n -> 1/(k * :math.pow(n+1, 2*k)) end
     ukn = fn k, n -> Enum.sum(Enum.map(1..n, fn x -> vkn.(k, x) end)) end
     skn = fn k, n -> Enum.sum(Enum.map(1..k, fn x -> ukn.(x, n) end)) end
     skn.(maxk, maxn)
    end

end
