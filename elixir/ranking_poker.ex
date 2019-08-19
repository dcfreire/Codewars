defmodule PokerHand do
  @result %{win: 1, loss: 2, tie: 3}
  @cards %{"T" => "10", "J" => "11", "Q" => "12", "K" => "13", "A" => "1", "D" => "0", "H" => "1", "C" => "2", "S" => "3"}
  def compare(player, opponent) do
    player = Enum.chunk(Enum.filter(String.codepoints(player), fn x -> x != " " end), 2)
    |> Enum.map(fn [a, b] -> {Map.get(@cards, a, a), Map.get(@cards, b, b)} end)
    opponent = Enum.chunk(Enum.filter(String.codepoints(opponent), fn x -> x != " " end), 2)
    |> Enum.map(fn [a, b] -> {Map.get(@cards, a, a), Map.get(@cards, b, b)} end)
    opponent =  Enum.map(0..Enum.count(opponent) -1, fn x -> {Enum.at(opponent, x), Enum.count(opponent, fn k -> elem(k, 0) == elem(Enum.at(opponent, x), 0) end)} end)
    |> Enum.sort_by(&(elem(&1, 1)), &>=/2)
    player =  Enum.map(0..Enum.count(player) -1, fn x -> {Enum.at(player, x), Enum.count(player, fn k -> elem(k, 0) == elem(Enum.at(player, x), 0) end)} end)
    |> Enum.sort_by(&(elem(&1, 1)), &>=/2)
  end

end
