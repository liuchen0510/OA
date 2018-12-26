package com.webtest.demo;
import java.io.IOException;
import com.webtest.core.WebDriverEngine;
import com.webtest.utils.ReadProperties;
public class Login_Action {
	private WebDriverEngine webtest;
	  public Login_Action(WebDriverEngine webtest) {
		  this.webtest=webtest;
	  }
	  public void login(String email,String password) throws IOException 
	  {
		  	webtest.open(ReadProperties.getPropertyValue("base_url"));
			webtest.type("id=vipname", email);
			webtest.type("id=vippassword", password);
			webtest.click("link=µÇÂ¼");
		
	  }

}
