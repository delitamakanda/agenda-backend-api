import { Component, OnInit } from '@angular/core';
import { DatePipe } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-agenda',
  templateUrl: 'agenda.page.html',
  styleUrls: ['agenda.page.scss']
})
export class AgendaPage implements OnInit {

  dates: Date[];
  dateEnd: Date;
  dateBegin: Date;
  dateBeginActive = new Date().getDay();
  dateActive: Date;

  countWeek = 1;
  countselect = 0;

  constructor(
    private datePipe: DatePipe,
    private router: Router
  ) {}

  ngOnInit() {
    this.initializeDates();
  }

  initializeDates() {
    this.dateBegin = this.getPreviousMonday();
    this.dateEnd = new Date(this.dateBegin);
    this.dateEnd.setDate(this.dateEnd.getDate() + 6);
    this.dates = [];

    const dateFrom = this.dateBegin;
    const dateTo = this.dateEnd;
    dateTo.setDate(dateTo.getDate() + 60);

    while (dateFrom <= dateTo) {
      this.dates.push(new Date(dateFrom));
      dateFrom.setDate(dateFrom.getDate() + 1);
    }
  }


  getPreviousMonday() {
    const prevMonday = new Date();
    prevMonday.setDate(prevMonday.getDate() - (prevMonday.getDay() + 6) % 7);

    return prevMonday;
  }

}
