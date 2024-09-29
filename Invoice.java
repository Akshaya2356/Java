public class Invoice 
{
    private String partNumber;
    private String partDescription;
    private int quantity;
    private double pricePerItem;

    public Invoice(String partNumber, String partDescription, int quantity, double pricePerItem) 
    {
        this.partNumber = partNumber;
        this.partDescription = partDescription;
        this.quantity = quantity;
        this.pricePerItem = pricePerItem;
    }
    public double getInvoiceAmount() 
    {
        return quantity * pricePerItem;
    }
    public String getPartNumber() 
    {
        return partNumber;
    }
    public String getPartDescription() 
    {
        return partDescription;
    }
    public double getPricePerItem() 
    {
        return pricePerItem;
    }
    public int getQuantity() 
    {
        return quantity;
    }
}
