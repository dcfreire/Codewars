defmodule StringMix do

  def mix(s1, s2) do
   comparator = fn s1,s2 -> if String.length(s1)==String.length(s2),
                           do:   s1 <= s2,
                          else: String.length(s1) >= String.length(s2)
                          end
    Enum.uniq(String.codepoints(s1 <> s2))
    |> Enum.filter(fn x -> x =~ ~r/^\p{Ll}$/u end)
    |> Enum.map(fn x ->
     ns1 = Enum.count(String.codepoints(s1), fn y -> x==y end)
     ns2 = Enum.count(String.codepoints(s2), fn y -> x==y end)
     cond do
      (ns1 == 1 or ns1 == 0) and (ns2 == 1 or ns2 == 0) ->
       0
      ns1 > ns2 ->
       {ns1, {"1", x}}
      ns1 < ns2 ->
       {ns2, {"2", x}}
      true ->
       {ns1, {"=", x}}
     end
    end)
    |> Enum.filter(fn x-> x != 0 end)
    |> Enum.map(fn x -> elem(elem(x, 1), 0) <> ":" <> String.duplicate(elem(elem(x, 1), 1), elem(x, 0)) <>  "/" end)
    |> Enum.sort(comparator)
    |> List.to_string()
    |> String.trim_trailing("/")
  end

end
