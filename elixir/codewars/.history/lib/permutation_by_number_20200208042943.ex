defmodule Factorial do
  def of(0), do: 1
  def of(n) when n > 0, do: n * of(n - 1)
end

defmodule Kata do
  def permutation_by_number() do
    ""
  end

  def permutation_by_number(word, n) do
    word
    |> String.graphemes()
    |> Enum.sort()
    |> List.to_string()
    |> Kata.permutation_by_number(n, [])
  end

  def permutation_by_number(word, _n, current) when byte_size(word) == 0 do
    current
    |> Enum.reverse()
    |> List.to_string()
  end

  def permutation_by_number(word, n, current) do
    freq =
      word
      |> String.graphemes()
      |> tl()
      |> Enum.uniq()
      |> (&Enum.reduce(&1, %{}, fn char, acc ->
            Enum.count(tl(String.graphemes(word)), fn x ->
              x == char
            end)
            |> (fn x -> Map.put(acc, char, x) end).()
          end)).()

    div(
      Factorial.of(Enum.sum(Map.values(freq))),
      Enum.reduce(freq, 1, fn x, acc ->
        Factorial.of(elem(x, 1)) * acc
      end)
    )
    |> (&(cond do
            &1 <= n ->
              try do
                String.graphemes(word)
                |> (fn y ->
                      List.pop_at(y, Enum.find_index(y, fn x -> x > hd(y) end))
                      |> (fn k -> [elem(k, 0) | elem(k, 1)] end).()
                    end).()
                |> List.to_string()
                |> Kata.permutation_by_number(
                  n - &1,
                  current
                )
              rescue
                _ in FunctionClauseError -> permutation_by_number()
              end

            &1 > n ->
              String.graphemes(word)
              |> List.pop_at(0)
              |> (fn x ->
                    Kata.permutation_by_number(List.to_string(Enum.sort(elem(x, 1))), n, [
                      elem(x, 0) | current
                    ])
                  end).()

            true ->
              nil
          end)).()
  end
end
