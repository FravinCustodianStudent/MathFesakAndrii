namespace Lab1._3.Models;

public class Film
{
    public int Views { get; set; }
    public int Frequency { get; set; }
    public int CumalativeFrequency { get; set; }
    public Film(int views,int cumFrequency)
    {
        Views = views;
        Frequency = 1;
        CumalativeFrequency = cumFrequency;

    }

    public static void WriteFilmsFrequency(List<Film> films,StreamWriter streamWriter)
    {
        streamWriter.WriteLine("Views | Frequency |      Cumulative frequency");
        int Cum = 0;
        for (int i = 0; i < films.Count; i++)
        {
            Cum += films[i].Frequency;
            if (i == 0)
                streamWriter.WriteLine($"{films[i].Views}  | {films[i].Frequency} |      {films[0].Frequency}");
            else
                streamWriter.WriteLine($"{films[i].Views}  | {films[i].Frequency} |      {Cum}");
        }
        streamWriter.WriteLine("Mode: " + films.MaxBy(m=>m.Frequency).Views);
        streamWriter.WriteLine("Median: "+ films[Convert.ToInt32(films.Count/2)].Views);
        streamWriter.WriteLine("Deviation: "+ Film.GetDeviation(films));
        streamWriter.WriteLine("Average squared difference: "+ Math.Sqrt(Film.GetDeviation(films)));
    }

    public static float GetDeviation(List<Film> films)
    {
        float res = 0, average = 0;
        foreach (var item in films)
        {
            res += (Convert.ToInt32(Math.Pow(item.Views,2))) * item.Frequency;
            average += item.Views*item.Frequency;
        }
        
        average /= films.Sum(a=>a.Frequency);
        res /= films.Sum(a=>a.Frequency);
        res -= average*average;
        return res;
    }

    public static bool operator ==(Film obj1, Film obj2)
    {
        if (obj1.Views == obj2.Views)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    public static bool operator !=(Film obj1, Film obj2)
    {
        return !(obj1 == obj2);
    }

    public static int FindMode(List<Film> films)
    {
        return films.MaxBy(m=>m.Frequency).Views;
    } 
}