USE Projeto;

delimiter |
CREATE TRIGGER tx_triger AFTER INSERT ON Transaction
	FOR EACH ROW
    BEGIN
		UPDATE
			Stock
		SET
			Stock.quantity = Stock.quantity + NEW.quantity
		WHERE
			Stock.id = NEW.stock_id;
	END;
|