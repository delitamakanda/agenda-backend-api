import { Component } from '@angular/core';

@Component({
  selector: 'app-news-page',
  templateUrl: 'news.page.html',
  styleUrls: ['news.page.scss']
})
export class NewsPage {

  constructor() {}

  errorImage(evt: any) {
    console.log('evt', evt);
    
  }

}
