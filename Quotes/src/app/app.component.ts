import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  quotes = [
    new Quote(1, 'All our dreams can come true, if we have the courage to pursue them.',' Walt Disney', "W.D"),
    new Quote(2, 'The secret of getting ahead is getting started.', 'Mark Twain',"M.T"),
    new Quote(3, '“It’s hard to beat a person who never gives up.', 'Babe Ruth',"B.R"),
    new Quote(4, 'Work like there is someone working twenty four hours a day to take it away from you.', 'Mark Cuban',"M.C"),
    new Quote(5, 'Very often, a change of self is needed more than a change of scene.', 'L.H.Holts',"A.C.Benson"),
];
  constructor(){  }
}
