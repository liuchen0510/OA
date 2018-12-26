package com.webtest.demo;
import java.io.IOException;

import com.webtest.core.WebDriverEngine;
import com.webtest.utils.ReadProperties;
public class AddMeeting_Action {
	private WebDriverEngine webtest;
	  public  AddMeeting_Action(WebDriverEngine webtest) {
		  this.webtest=webtest;
	  }
	  public void login(String email,String password) throws IOException 
	  {
		  	webtest.open(ReadProperties.getPropertyValue("base_url"));
			webtest.type("id=vipname", email);
			webtest.type("id=vippassword", password);
			webtest.click("link=登录");
	  }
	  public void add(String name) {
		    webtest.click("id=_M10");
		    webtest.click("link=会议室设置");
		    webtest.enterFrame("rightMain");
		    webtest.type("xpath=//input[@value='01']",name);
		    webtest.click("xpath=//input[@value='保存']");
	  }
}
