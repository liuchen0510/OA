package com.webtest.demo;
import static org.testng.Assert.assertTrue;
import org.testng.Assert;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Listeners;
import org.testng.annotations.Test;
import com.webtest.core.BaseTest;
import com.webtest.core.WebTestListener;
@Listeners(WebTestListener.class)
public class LoginTest extends BaseTest{
	Login_Action action;
	@BeforeMethod
	public void setup() {
		action=new Login_Action(webtest);
		
	}
	@Test(priority=0)
	public void LoginSuccess() throws Exception  {
		Login_Action action =new Login_Action(webtest);
		action.login("admin", "123456");
		assertTrue(webtest.ifContains("µÇÂ½³É¹¦"));
	}
	@Test(priority=1)
	public void LoginFail() throws Exception  {
		Login_Action action =new Login_Action(webtest);
		action.login("admin", "654321");
		assertTrue(webtest.ifContains("µÇÂ½Ê§°Ü"));
	}
}
