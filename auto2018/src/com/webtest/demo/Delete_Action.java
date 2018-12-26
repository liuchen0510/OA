package com.webtest.demo;

import java.io.IOException;

import com.webtest.core.WebDriverEngine;
import com.webtest.utils.ReadProperties;
	public class Delete_Action {
	private WebDriverEngine webtest;
	  public  Delete_Action(WebDriverEngine webtest) {
		  this.webtest=webtest;
	  }
	  public void login(String email,String password) throws IOException 
	  {
		  	webtest.open(ReadProperties.getPropertyValue("base_url"));
			webtest.type("id=vipname", email);
			webtest.type("id=vippassword", password);
			webtest.click("link=��¼");
	  }
	  public void delete1() {
		    webtest.click("id=_M10");
		  	webtest.click("link=ͶƱ");
		  	webtest.enterFrame("rightMain");
		  	webtest.click("xpath=//input[@value='19']");
		  	webtest.click("xpath=//input[@value='24']");
		  	webtest.click("xpath=//button[@action='cancel_concern']");
		  	
	  }
	  public void delete2() {
		    webtest.click("id=_M10");
		  	webtest.click("link=ͶƱ");
		  	webtest.enterFrame("rightMain");
		  	webtest.click("xpath=//input[@name='chkall']");
		  	webtest.click("xpath=//button[@action='cancel_concern']");
		  	
	  }
}
