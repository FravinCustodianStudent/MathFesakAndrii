using Lab1._3.Models;
using Microsoft.AspNetCore.Mvc;

namespace Lab1._3.Controllers;

[ApiController]
[Route("[controller]")]
public class FilmController : ControllerBase
{
    private string BasePath = "~/task_01_data/";
    private string BaseFile = "input_100.txt";
    [HttpGet]
    public async Task<List<Film>> GetData()
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
        return films;
    }
    [HttpGet]
    [Route("/deviation")]
    public async Task<float> GetDeviation()
    {
        return Film.GetDeviation(await GetData(BaseFile));
    }
    [Route("/mode")]
    public async Task<int> GetMode()
    {
        return Film.FindMode(await GetData(BaseFile));
    }
}