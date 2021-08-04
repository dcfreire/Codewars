defmodule VowelCount do
  def get_count(str) do
    Enum.count(String.to_charlist(str), fn x -> Enum.member?(String.to_charlist("aeiou"), x) end)
  end
end
