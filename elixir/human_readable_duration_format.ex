defmodule DurationFormatter do
  def format_duration(seconds) do
    year = div(seconds, 31_536_000)
    seconds_rem = seconds - year * 31_536_000
    day = div(seconds_rem, 86400)
    seconds_rem = seconds_rem - day * 86400
    hour = div(seconds_rem, 3600)
    seconds_rem = seconds_rem - hour * 3600
    minute = div(seconds_rem, 60)
    seconds_rem = seconds_rem - minute * 60
    words = ["year", "day", "hour", "minute", "second"]
    numbers = [year, day, hour, minute, seconds_rem]

    str =
      Enum.map(0..(Enum.count(numbers) - 1), fn x ->
        cond do
          Enum.at(numbers, x) > 0 ->
            Kernel.inspect(Enum.at(numbers, x)) <>
              " " <>
              Enum.at(words, x) <>
              cond do
                Enum.at(numbers, x) > 1 ->
                  "s"

                true ->
                  ""
              end

          true ->
            ""
        end
      end)
      |> Enum.filter(fn x -> String.length(x) > 0 end)
      |> Enum.intersperse(", ")

    str =
      Enum.map(0..(Enum.count(str) - 1), fn x ->
        cond do
          x == Enum.count(str) - 2 and Enum.at(str, x) == ", " ->
            " and "

          true ->
            Enum.at(str, x)
        end
      end)

    if Enum.count(str) == 2 do
      "now"
    else
      List.to_string(str)
    end
  end
end
