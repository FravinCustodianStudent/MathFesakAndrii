import { Component, Inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {deviation} from "d3";

@Component({
  selector: 'app-fetch-data',
  templateUrl: './fetch-data.component.html'
})
export class FetchDataComponent{
  public films: Film[] = [];
  public filmCumulativeFrequency: number[] = [];
  public filmsCharts:any[] = [];
  public mode:number = 0;
  public dev:number = 0;
  public devSqrt: number =0;
  public median: number = 0;
  public ss  = [
    {
      "name": "book",
      "value" : 3
    }
  ]
  constructor(http: HttpClient, @Inject('BASE_URL') baseUrl: string) {
    http.get<Film[]>(baseUrl + 'weatherforecast').subscribe(result => {
      console.log(result);
      this.films = result;
      for (let i = 0; i < this.films.length; i++) {

        this.filmsCharts.push({
          name: String(this.films[i].views),
          value: this.films[i].frequency
        });
        this.ss = [...this.filmsCharts]
      }
      console.log(this.filmsCharts)
    }, error => console.error(error));
    http.get<number>(baseUrl+'weatherforecast/deviation').subscribe(result => {
      this.dev = result;
      this.devSqrt =Math.round(Math.sqrt(this.dev) * 100) / 100 ;

    }, error => console.error(error));
    http.get<number>(baseUrl+'weatherforecast/mode').subscribe(result => {
      this.mode = result;
    }, error => console.error(error));
    http.get<number>(baseUrl+'weatherforecast/med').subscribe(result => {
      this.median = result;
      console.log(this.ss);
    }, error => console.error(error));
  }
}

interface Film{
  views: number;
  frequency: number;
  cumalativeFrequency: number;
}
class FilmChart{
  name: string = "";
  value: number = 0;
}
