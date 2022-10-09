using Lab1._3.Models;
using Microsoft.AspNetCore.Mvc;

namespace Lab1._3.Controllers;

[ApiController]
[Route("[controller]")]
public class WeatherForecastController : ControllerBase
{
    private string BasePath = "../Lab1.3/task_01_data/";
    private string BaseFile = "input_10.txt";
    [HttpGet]
    public async Task<List<Film>> Index()
    {
        return await GetData(BaseFile);
    }
    public async Task<List<Film>> GetData(string path)
    {
        var films = new List<Film>();
        using (StreamReader reader = new StreamReader(BasePath+path))
        {
            string line;
            int i = 1;
            while ((line = await reader.ReadLineAsync()) != null)
            {
                bool exist = false;
                for (int j = 0; j < films.Count; j++)
                {
                    if (films[j].Views == Convert.ToInt32(line) )
                    {
                        films[j].Frequency++;
                        exist = true;
                    }
                }

                if (!exist)
                {
                    var film = new Film(Convert.ToInt32(line),1);
                    films.Add(film);
                }

            }
        }

        int sum = films[0].Frequency;
        for (int i = 0; i < films.Count; i++)
        {
            
            if (i!=0)
            {
                films[i].CumalativeFrequency = sum + films[i].Frequency;
            }
            else
            {
                films[i].CumalativeFrequency = sum;
                continue;
            }

            sum += films[i].Frequency;
        }
        return films;
    }
    [HttpGet("deviation")]
    public async Task<float> GetDeviation()
    {
        return Film.GetDeviation(await GetData(BaseFile));
    }

    [HttpGet("med")]
    public async Task<int> GetMedian()
    {
        var films = await GetData(BaseFile);
        return films[Convert.ToInt32(films.Count / 2)].Views;
    }
    [HttpGet("mode")]
    public async Task<int> GetMode()
    {
        return Film.FindMode(await GetData(BaseFile));
    }
}