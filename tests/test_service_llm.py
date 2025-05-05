from unittest.mock import MagicMock, patch

from src.service_llm import summarize_large_text, summarize_small_text


@patch("src.service_llm.init_chat_model")
@patch("src.service_llm.create_stuff_documents_chain")
def test_summarize_small_text(mock_create_chain, mock_init_chat_model):
    mock_llm = MagicMock()
    mock_init_chat_model.return_value = mock_llm

    mock_chain = MagicMock()
    mock_chain.invoke.return_value = "Summary of a small text."
    mock_create_chain.return_value = mock_chain

    small_text = "This is a small text."
    result = summarize_small_text(small_text)
    expected = "Summary of a small text."

    assert result == expected

    mock_create_chain.assert_called_with(
        mock_llm,
        mock_create_chain.call_args[0][1]
    )


@patch("src.service_llm.init_chat_model")
@patch("src.service_llm.create_stuff_documents_chain")
def test_summarize_large_text(mock_create_chain, mock_init_chat_model):
    mock_llm = MagicMock()
    mock_init_chat_model.return_value = mock_llm

    mock_chain = MagicMock()
    mock_chain.invoke.return_value = "Summary of a very long text."
    mock_create_chain.return_value = mock_chain

    long_text = "Lorem ipsum " * 100  # Create a long text that exceeds the threshold
    result = summarize_large_text(long_text)

    expected = "Summary of a very long text."

    assert result == expected

    mock_create_chain.assert_called_with(
        mock_llm,
        mock_create_chain.call_args[0][1]
    )
