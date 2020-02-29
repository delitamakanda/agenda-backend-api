import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TabsPage } from './tabs.page';

const routes: Routes = [
  {
    path: 'tabs',
    component: TabsPage,
    children: [
      {
        path: 'tab1',
        children: [
          {
            path: '',
            loadChildren: () =>
              import('../../pages/news/news.module').then(m => m.NewsPageModule)
          }
        ]
      },
      {
        path: 'tab2',
        children: [
          {
            path: '',
            loadChildren: () =>
              import('../../pages/tab2/tab2.module').then(m => m.Tab2PageModule)
          }
        ]
      },
      {
        path: 'agenda',
        children: [
          {
            path: '',
            loadChildren: () =>
              import('../../pages/agenda/agenda.module').then(m => m.AgendaPageModule)
          }
        ]
      },
      {
        path: 'venue',
        children: [
          {
            path: '',
            loadChildren: () => import('../../pages/venue/venue.module').then( m => m.VenuePageModule)
          }
        ]
      },
      {
        path: 'contact',
        children: [
          {
            path: '',
            loadChildren: () => import('../../pages/contact/contact.module').then( m => m.ContactPageModule)
          }
        ]
      },
      {
        path: '',
        redirectTo: '/tabs/tab1',
        pathMatch: 'full'
      }
    ]
  },
  {
    path: '',
    redirectTo: '/tabs/tab1',
    pathMatch: 'full'
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TabsPageRoutingModule {}
