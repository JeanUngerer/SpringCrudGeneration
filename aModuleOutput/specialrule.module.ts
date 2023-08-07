import { NgModule } from '@angular/core';
import { SpecialRuleListComponent } from './specialrulelistcomponent/specialrulelistcomponent.component';
import { SpecialRuleDetailComponent } from './specialruledetailcomponent/specialruledetailcomponent.component';
import { SpecialRuleCreateComponent } from './specialrulecreatecomponent/specialrulecreatecomponent.component';

@NgModule({
	declarations: [
		SpecialRuleListComponent,
		SpecialRuleDetailComponent,
		SpecialRuleCreateComponent,
	],
	exports: [
		SpecialRuleListComponent,
		SpecialRuleDetailComponent,
		SpecialRuleCreateComponent,
	]
})
export class SpecialRuleModule { }
