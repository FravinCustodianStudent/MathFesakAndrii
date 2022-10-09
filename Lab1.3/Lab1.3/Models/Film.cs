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

    public static void WriteFilmsFrequency(List<Film> films)
    {
        Console.WriteLine("Views | Frequency |      Cumulative frequency");
        int Cum = 0;
        for (int i = 0; i < films.Count; i++)
        {
            Cum += films[i].Frequency;
            if (i == 0)
                Console.WriteLine($"{films[i].Views}  | {films[i].Frequency} |      {films[0].Frequency}");
            else
                Console.WriteLine($"{films[i].Views}  | {films[i].Frequency} |      {Cum}");
        }
        
    }

    public static float GetDeviation(List<Film> films)
    {
        float res = 0,average=0;
        foreach (var item in films)
        {
            res += (Convert.ToInt32(Math.Pow(item.Views,2))) * item.Frequency;
            average += item.Views;
        }
        average /= films.Count;
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
        List<int> numbers = new List<int>();
        List<int> frequence = new List<int>();

        for (int i = 0; i < films.Count; i++)
        {
            if (numbers.Contains(films[i].Views))
            {

                for (int j = 0; j < numbers.Count; j++)
                {
                    if (numbers[j] == films[i].Views)
                    {
                        frequence[j]++;
                    }
                    
                }
            }
            else
            {
                numbers.Add(films[i].Views);
                frequence.Add(1);
            }

            
        }
        var a = frequence.Max();
        for (int j = 0; j < frequence.Count; j++)
        {
            if (frequence[j]==a)
            {
                return numbers[j];
            }
        }
        return 0;
    } 
}