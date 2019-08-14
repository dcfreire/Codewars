defmodule Mumbling do

  def accum(s) do
   String.capitalize(String.at(s, 0)) <> List.to_string(Enum.map(1..String.length(s)-1, fn x -> "-" <> String.capitalize(String.duplicate(Enum.at(String.graphemes(s), x), x+1)) end))
  end

end
