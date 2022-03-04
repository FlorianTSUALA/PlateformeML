<span class="light-logo"><img src="{% static 'template/images/logo-dark-text.png' %}" alt="logo"></span>
{% csrf_token %}




{% block floating-button %}

    {% if url_create %}
        {% include "includes/floating-add-button.html" %}
    {% endif %}

{% endblock %}


{% include "partials/model/list.html" %}		


section_item_title
section_title
{% url url_create %}


<script src="{% static 'custom/js/entity.js' %}"></script>
<script>
  $("#form_model .select2").select2({
    dropdownParent: $("#modal-entity")
    });
</script>


{% block javascript %}

{% endblock %}




{% block page_scripts %}
  
{% endblock %}