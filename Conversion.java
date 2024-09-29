import java.util.*;
class Converter
{
}
class CurrencyConverter extends Converter
{
	double dollarToINR(double dollar) 
  {
		return dollar * 83;
	}
	double EuroToINR(double euro)
  {
		return euro * 90;
	}	
	double YENToINR(double yen)
  {
		return yen * 0.56;
	}	
	double INRToDollar(double inr) 
  {
		return inr * 0.012;
	}	
	double INRToEuro(double inr)
  {
		return inr / 90;
	}
	double INRToYEN(double inr)
  {
		return inr / 0.56;
	}
}
class TimeConverter extends Converter
{	
	int hoursToMin(int hrs) 
  {
		return hrs * 60;
	}	
	int minToSec(int mins)
  {
		return mins * 60;
	}	
	int hrsToSec(int hrs) 
  {
		return hrs * 3600;
	}	
	int minsToHr(int mins) 
  {
		return mins / 60;
	}	
	int secsToHr(int secs) 
  {
		return secs / 3600;
	}	
	int secsToMin(int secs) 
  {
		return secs / 60;
	}
}
class DistanceConverter extends Converter
{
	double meterToKm(double meter) 
  {
		return meter / 1000;
	}	
	double KmToMeter(double kiloMeters) 
  {
		return kiloMeters * 1000;
	}
	double KmToMile(double kilometers) 
  {
		return kilometers * 0.621371;
	}	
	double milesToKm(double miles) 
  {
		return miles / 0.621371;
	}
}
public class Conversion 
{
	public static void main(String s[]) 
  {
		Scanner sc = new Scanner(System.in);
		System.out.println("Currency Conversion (Dollar to INR): ");
    System.out.println("Enter amount in USD: ");
		CurrencyConverter currency = new CurrencyConverter();
		System.out.println("Rupees :" + currency.dollarToINR(sc.nextDouble()));

		System.out.println("\nTime Conversion (Hours to Minutes): ");
    System.out.println("Enter time in hours: ");
		TimeConverter timeConverter = new TimeConverter();
		System.out.println("Minutes: "+ timeConverter.hoursToMin(sc.nextInt()));

		System.out.println("\nDistance Conversion (Meter to KM): ");
    System.out.println("Enter distance in meters: ");
    DistanceConverter distanceConverter = new DistanceConverter();
    System.out.println("Kilo meters: " + distanceConverter.meterToKm(sc.nextDouble()));
	}
}
